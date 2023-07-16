from flask import Flask, request, jsonify, render_template, send_file
from azure.cosmos import CosmosClient
from flask_cors import CORS
import string
import random
import os
from dotenv import load_dotenv
from emograph import make_emotion_graph
from reagraph import make_reaction_graph
import datetime
import pytz



load_dotenv()

app = Flask(__name__, static_folder="./build/static", template_folder="./build/templates/")
CORS(app)  # CORSを有効にする（異なるオリジンからのリクエストを許可）

# Cosmos DB の接続情報を指定します
endpoint = os.getenv("ENDPOINT")
key = os.getenv("KEY")
database_name = "REmetor-Backend"
container_name = "Rooms"

# Cosmos DB に接続します
client = CosmosClient(endpoint, key)

# Cosmos DBのコンテナを取得します
container = client.get_database_client(database_name).get_container_client(container_name)

try:
    if time_summary_dict_emotion == {}:
        pass
    else:
        pass
except:
    # 時間ごとのサマリー結果をpoolするための辞書を作成します
    time_summary_dict_emotion = {}
    
try:
    if time_summary_dict_reaction == {}:
        pass
    else:
        pass
except:
    # 時間ごとのサマリー結果をpoolするための辞書を作成します
    time_summary_dict_reaction = {}


@app.route("/", methods=["GET"])
def hello():
    # index.htmlをレンダリングして表示します
    return render_template("index.html")

@app.route("/createRoom/", methods=["POST"])
def create_room():
    # POSTリクエストから部屋の情報を取得します
    data = request.json
    room_name = data["Roomname"]
    description = data["Description"]
    host_name = data["HostName"]
    password = data["Password"]
    room_id = data["id"]

    # Cosmos DBのコンテナに部屋の情報を作成します
    container.create_item(
        {
            "id": room_id,
            "Id": room_id,
            "Roomname": room_name,
            "Description": description,
            "HostName": host_name,
            "Password": password,
            "ActionsList": [],
        }
    )

    return "success"

@app.route("/getActionsList/", methods=["GET"])
def get_action():
    # GETリクエストからroom_idを取得します
    room_id = request.args.get("room_id")

    # Cosmos DBから指定されたroom_idのActionsListを取得します
    query = {'query': f'SELECT c.ActionsList FROM c WHERE c.id = "{room_id}"'}
    items = list(container.query_items(query, enable_cross_partition_query=True))
    # items.insert(0, {"id": room_id})
    items.reverse()
    print(items)
    try:
        if len(items) > 0:
            return {"items": items}
        else:
            return {"items": []}
    except:
        return {"items": []}

@app.route("/getSummaryEmotion/", methods=["GET"])
def get_summary_emotion():
    # GETリクエストからroom_idを取得します
    room_id = request.args.get("room_id")

    # Cosmos DBから指定されたroom_idのActionsListを取得します
    query = {'query': f'SELECT c.ActionsList FROM c WHERE c.id = "{room_id}"'}
    items = list(container.query_items(query, enable_cross_partition_query=True))

    # エモーションの数値ごとのカウントを格納する辞書を作成します
    emotional_value_dict = {}

    # エモーションの数値ごとにカウントを増やします
    # print("items", items)
    try:
        for item in items[0]["ActionsList"]:
            if str(item["Emotion"]) in list(emotional_value_dict.keys()):
                emotional_value_dict[item["Emotion"]] += 1
            else:
                emotional_value_dict[item["Emotion"]] = 1
    except:
        return {"items": {"value": [], "rate": []}}

    items_number = sum(emotional_value_dict.values())  # アイテムの総数

    # エモーションの割合を格納する辞書を作成します
    emotional_rate_dict = {}

    # エモーションの割合を計算します
    for key in list(emotional_value_dict.keys()):
        emotional_rate_dict[key] = emotional_value_dict[key] / items_number

    emotional_value_result_list = []

    # エモーションの数値ごとのカウントを辞書からリストに変換します
    for key in list(emotional_value_dict.keys()):
        emotional_value_result_dict = {}
        emotional_value_result_dict["name"] = key
        emotional_value_result_dict["value"] = emotional_value_dict[key]
        emotional_value_result_list.append(emotional_value_result_dict)

    emotional_rate_result_list = []

    # エモーションの割合を辞書からリストに変換します
    for key in list(emotional_rate_dict.keys()):
        emotional_rate_result_dict = {}
        emotional_rate_result_dict["name"] = key
        emotional_rate_result_dict["value"] = int(emotional_rate_dict[key] * 100)
        emotional_rate_result_list.append(emotional_rate_result_dict)

    dt = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    time_summary_dict_emotion[dt.strftime('%Y-%m-%d %H:%M:%S')]={"value": emotional_value_result_list, "rate": emotional_rate_result_list}
    print(time_summary_dict_emotion.keys())
    print(time_summary_dict_emotion)
    try:
        MRG = make_emotion_graph(time_summary_dict=time_summary_dict_emotion, file_path="assets/"+room_id+"/result_emotion.png")
        MRG.run()
    except:
        try:
            os.mkdir("assets/"+room_id)
        except FileExistsError:
            pass
        MRG = make_emotion_graph(time_summary_dict=time_summary_dict_emotion, file_path="assets/"+room_id+"/result_emotion.png")
        MRG.run()
    return {"items": {"value": emotional_value_result_list, "rate": emotional_rate_result_list}}


@app.route("/getSummaryReaction/", methods=["GET"])
def get_summary_reaction():
    # GETリクエストからroom_idを取得します
    room_id = request.args.get("room_id")
    print(room_id)

    # Cosmos DBから指定されたroom_idのActionsListを取得します
    query = {'query': f'SELECT c.ActionsList FROM c WHERE c.id = "{room_id}"'}
    items = list(container.query_items(query, enable_cross_partition_query=True))

    # エモーションの数値ごとのカウントを格納する辞書を作成します
    emotional_value_dict = {}

    # エモーションの数値ごとにカウントを増やします
    # print("items", items)
    try:
        for item in items[0]["ActionsList"]:
            if str(item["Reaction"]) in list(emotional_value_dict.keys()):
                emotional_value_dict[item["Reaction"]] += 1
            else:
                emotional_value_dict[item["Reaction"]] = 1
    except:
        return {"items": {"value": [], "rate": []}}

    items_number = sum(emotional_value_dict.values())  # アイテムの総数

    # エモーションの割合を格納する辞書を作成します
    emotional_rate_dict = {}

    # エモーションの割合を計算します
    for key in list(emotional_value_dict.keys()):
        emotional_rate_dict[key] = emotional_value_dict[key] / items_number

    emotional_value_result_list = []

    # エモーションの数値ごとのカウントを辞書からリストに変換します
    for key in list(emotional_value_dict.keys()):
        emotional_value_result_dict = {}
        emotional_value_result_dict["name"] = key
        emotional_value_result_dict["value"] = emotional_value_dict[key]
        emotional_value_result_list.append(emotional_value_result_dict)

    emotional_rate_result_list = []

    # エモーションの割合を辞書からリストに変換します
    for key in list(emotional_rate_dict.keys()):
        emotional_rate_result_dict = {}
        emotional_rate_result_dict["name"] = key
        emotional_rate_result_dict["value"] = int(emotional_rate_dict[key] * 100)
        emotional_rate_result_list.append(emotional_rate_result_dict)

    dt = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    time_summary_dict_reaction[dt.strftime('%Y-%m-%d %H:%M:%S')]={"value": emotional_value_result_list, "rate": emotional_rate_result_list}
    print(time_summary_dict_reaction.keys())
    print(time_summary_dict_reaction)
    try:
        MRG = make_reaction_graph(time_summary_dict=time_summary_dict_reaction, file_path="assets/"+room_id+"/result_reaction.png")
        MRG.run()
    except:
        try:
            os.mkdir("assets/"+room_id)
        except FileExistsError:
            pass
        MRG = make_reaction_graph(time_summary_dict=time_summary_dict_reaction, file_path="assets/"+room_id+"/result_reaction.png")
        MRG.run()
    return {"items": {"value": emotional_value_result_list, "rate": emotional_rate_result_list}}


@app.route('/GetEmotionGraph/', methods=["GET"])
def get_emotion_graph():
    room_id = request.args.get("room_id")
    filename = 'result_emotion.png'  # この行に対象の写真のファイル名を指定してください
    return send_file('assets/' +room_id+"/"+ filename, mimetype='image/png')

@app.route('/GetReactionGraph/', methods=["GET"])
def get_reaction_graph():
    room_id = request.args.get("room_id")
    filename = 'result_reaction.png'  # この行に対象の写真のファイル名を指定してください
    return send_file('assets/'+room_id+"/"+ filename, mimetype='image/png')

if __name__ == "__main__":
    # アプリケーションをデバッグモードで実行し、ポート番号を環境変数から取得（デフォルトは5000）
    app.debug = True
    app.run(host='0.0.0.0', port=5001, threaded=True)