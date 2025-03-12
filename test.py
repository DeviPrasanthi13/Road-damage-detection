from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor

import cv2

model = YOLO("y8best.pt")

results = model.predict(source="sample_video.mp4", show=True)

print(results)











# # from ultralytics import YOLO
# # # from ultralytics.yolo.v8.detect.predict import DetectionPredictor
# # from flask import Flask

# # import cv2
# # app = Flask(__name__)
# # @app.route("/")
# # @app.route("/home")
# # def home():
# # model = YOLO("y8best.pt")

# # results = model.predict(source="sample_video.mp4", show=True)
# # # print(results)
# # return print(results)

# # if __name__ == '__main__':
# #     app.run(debug=True,port=5001)



# from ultralytics import YOLO
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# @app.route("/home")
# def home():
#     model = YOLO("y8best.pt")

#     results = model.predict(source="sample_video.mp4", show=True)
#     # print(results)
#     return str(results)  # Use str() to convert the results to a string for returning

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)


    

