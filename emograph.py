import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import os

import matplotlib.pyplot as plt

time_summary_dict={'2023-07-08 16:42:47': {'value': [{'name': 'Ctime_summary_dictALM', 'value': 28}, {'name': 'HAPPY', 'value': 2}, {'name': 'SAD', 'value': 4}, {'name': None, 'value': 1}, {'name': 'DISGUSTED', 'value': 1}, {'name': 'ANGRY', 'value': 1}, {'name': 'CONFUSED', 'value': 1}, {'name': 'SURPRISED', 'value': 1}], 'rate': [{'name': 'CALM', 'value': 71.7948717948718}, {'name': 'HAPPY', 'value': 5.128205128205128}, {'name': 'SAD', 'value': 10.256410256410255}, {'name': None, 'value': 2.564102564102564}, {'name': 'DISGUSTED', 'value': 2.564102564102564}, {'name': 'ANGRY', 'value': 2.564102564102564}, {'name': 'CONFUSED', 'value': 2.564102564102564}, {'name': 'SURPRISED', 'value': 2.564102564102564}]}, '2023-07-08 16:42:50': {'value': [{'name': 'CALM', 'value': 28}, {'name': 'HAPPY', 'value': 2}, {'name': 'SAD', 'value': 4}, {'name': None, 'value': 1}, {'name': 'DISGUSTED', 'value': 1}, {'name': 'ANGRY', 'value': 1}, {'name': 'CONFUSED', 'value': 1}, {'name': 'SURPRISED', 'value': 1}], 'rate': [{'name': 'CALM', 'value': 71.7948717948718}, {'name': 'HAPPY', 'value': 5.128205128205128}, {'name': 'SAD', 'value': 10.256410256410255}, {'name': None, 'value': 2.564102564102564}, {'name': 'DISGUSTED', 'value': 2.564102564102564}, {'name': 'ANGRY', 'value': 2.564102564102564}, {'name': 'CONFUSED', 'value': 2.564102564102564}, {'name': 'SURPRISED', 'value': 2.564102564102564}]}, '2023-07-08 16:42:53': {'value': [{'name': 'CALM', 'value': 28}, {'name': 'HAPPY', 'value': 2}, {'name': 'SAD', 'value': 4}, {'name': None, 'value': 1}, {'name': 'DISGUSTED', 'value': 1}, {'name': 'ANGRY', 'value': 1}, {'name': 'CONFUSED', 'value': 1}, {'name': 'SURPRISED', 'value': 1}], 'rate': [{'name': 'CALM', 'value': 71.7948717948718}, {'name': 'HAPPY', 'value': 5.128205128205128}, {'name': 'SAD', 'value': 10.256410256410255}, {'name': None, 'value': 2.564102564102564}, {'name': 'DISGUSTED', 'value': 2.564102564102564}, {'name': 'ANGRY', 'value': 2.564102564102564}, {'name': 'CONFUSED', 'value': 2.564102564102564}, {'name': 'SURPRISED', 'value': 2.564102564102564}]}, '2023-07-08 16:43:01': {'value': [{'name': 'CALM', 'value': 28}, {'name': 'HAPPY', 'value': 2}, {'name': 'SAD', 'value': 4}, {'name': None, 'value': 1}, {'name': 'DISGUSTED', 'value': 1}, {'name': 'ANGRY', 'value': 1}, {'name': 'CONFUSED', 'value': 1}, {'name': 'SURPRISED', 'value': 1}], 'rate': [{'name': 'CALM', 'value': 71.7948717948718}, {'name': 'HAPPY', 'value': 5.128205128205128}, {'name': 'SAD', 'value': 10.256410256410255}, {'name': None, 'value': 2.564102564102564}, {'name': 'DISGUSTED', 'value': 2.564102564102564}, {'name': 'ANGRY', 'value': 2.564102564102564}, {'name': 'CONFUSED', 'value': 2.564102564102564}, {'name': 'SURPRISED', 'value': 2.564102564102564}]}, '2023-07-08 16:43:03': {'value': [{'name': 'CALM', 'value': 28}, {'name': 'HAPPY', 'value': 2}, {'name': 'SAD', 'value': 4}, {'name': None, 'value': 1}, {'name': 'DISGUSTED', 'value': 1}, {'name': 'ANGRY', 'value': 1}, {'name': 'CONFUSED', 'value': 1}, {'name': 'SURPRISED', 'value': 1}], 'rate': [{'name': 'CALM', 'value': 71.7948717948718}, {'name': 'HAPPY', 'value': 5.128205128205128}, {'name': 'SAD', 'value': 10.256410256410255}, {'name': None, 'value': 2.564102564102564}, {'name': 'DISGUSTED', 'value': 2.564102564102564}, {'name': 'ANGRY', 'value': 2.564102564102564}, {'name': 'CONFUSED', 'value': 2.564102564102564}, {'name': 'SURPRISED', 'value': 2.564102564102564}]}, '2023-07-08 16:43:06': {'value': [{'name': 'CALM', 'value': 28}, {'name': 'HAPPY', 'value': 2}, {'name': 'SAD', 'value': 4}, {'name': None, 'value': 1}, {'name': 'DISGUSTED', 'value': 1}, {'name': 'ANGRY', 'value': 1}, {'name': 'CONFUSED', 'value': 1}, {'name': 'SURPRISED', 'value': 1}], 'rate': [{'name': 'CALM', 'value': 71.7948717948718}, {'name': 'HAPPY', 'value': 5.128205128205128}, {'name': 'SAD', 'value': 10.256410256410255}, {'name': None, 'value': 2.564102564102564}, {'name': 'DISGUSTED', 'value': 2.564102564102564}, {'name': 'ANGRY', 'value': 2.564102564102564}, {'name': 'CONFUSED', 'value': 2.564102564102564}, {'name': 'SURPRISED', 'value': 2.564102564102564}]}, '2023-07-08 16:43:09': {'value': [{'name': 'CALM', 'value': 28}, {'name': 'HAPPY', 'value': 2}, {'name': 'SAD', 'value': 4}, {'name': None, 'value': 1}, {'name': 'DISGUSTED', 'value': 1}, {'name': 'ANGRY', 'value': 1}, {'name': 'CONFUSED', 'value': 1}, {'name': 'SURPRISED', 'value': 1}], 'rate': [{'name': 'CALM', 'value': 71.7948717948718}, {'name': 'HAPPY', 'value': 5.128205128205128}, {'name': 'SAD', 'value': 10.256410256410255}, {'name': None, 'value': 2.564102564102564}, {'name': 'DISGUSTED', 'value': 2.564102564102564}, {'name': 'ANGRY', 'value': 2.564102564102564}, {'name': 'CONFUSED', 'value': 2.564102564102564}, {'name': 'SURPRISED', 'value': 2.564102564102564}]}}

class make_emotion_graph:
    def __init__(self, time_summary_dict=time_summary_dict, file_path="assets/result_emotion.png"):
        self.time_summary_dict = time_summary_dict
        self.emotion_list=["HAPPY", "SURPRISED", "CONFUSED", "ANGRY", "DISGUSTED", "FEAR","SAD", "CALM"]
        self.file_path = file_path
        # self.x, self.y = self.time_summary()
        # self.draw_plot()

    def time_summary(self):
        x = []
        y = {}
        for emotion in self.emotion_list:
            y[emotion] = []
        # タイムスタンプごとにループ
        for timestamp in self.time_summary_dict.keys():
            x.append(timestamp)
            for emotion in self.emotion_list:
                flag = False
                # print(x)
                for item in self.time_summary_dict[timestamp]['value']:
                    if item["name"] == emotion:
                        y[emotion].append(item["value"])
                        flag=True
                if flag == False:
                    y[emotion].append(0)
        return x,y

    def draw_plot(self,x,y):
        # Convert x-axis values to datetime objects
        x_datetime = [mdates.datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in x]

        # Set color scheme
        text_color = '#fcfffb'
        background_color = '#242424'
        primary_color = '#df929b'

        # Set plot style
        plt.style.use('seaborn-whitegrid')

        # Set figure and axes properties
        fig, ax = plt.subplots(figsize=(9, 5))
        fig.patch.set_facecolor(background_color)
        ax.set_facecolor(background_color)
        ax.spines[['top', 'right']].set_visible(False)

        # Plotting
        for i, (name, values) in enumerate(y.items()):
            color = plt.cm.tab10(i)  # Get color from default colormap
            ax.plot(x_datetime[1:], values[1:], label=name, color=color, linestyle='-', marker='o', markersize=5)

        # Set plot title
        # ax.set_title('Emotion Value Over Time', fontsize=16, fontweight='bold', color=text_color)

        # Set x-axis and y-axis labels
        ax.set_xlabel('Time', fontsize=12, color=text_color)
        ax.set_ylabel('Count', fontsize=12, color=text_color)

        # Format x-axis as dates
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
        ax.tick_params(axis='both', rotation=45, labelsize=10, colors=text_color)

        # Add grid lines
        ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

        # Add legend
        ax.legend(fontsize=12, facecolor=background_color, edgecolor=background_color, labelcolor=text_color, framealpha=0.7)

        # Adjust layout
        fig.tight_layout()

        # Set text color and background color
        plt.rcParams['text.color'] = text_color
        plt.rcParams['figure.facecolor'] = background_color

        # Show plot
        # plt.show()

        plt.savefig(self.file_path)

    def run(self):
        x,y=self.time_summary()
        self.draw_plot(x, y)

if __name__=='__main__':
    MG=make_reaction_graph()
    MG.time_summary()