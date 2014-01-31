# encoding:utf-8

# pythonからopencvを使いたい場合は事前に
#   raspbianなら: sudo apt-get install python-opencv
# とかしてpythonにopencvバインディングとその依存パッケージを
# システムに導入しておく必要があります。

# CV2(OpenCV2ライブラリー)を使いますよ
import cv2

# cameraって名前でVideoCaptureオブジェクトをデバイス0番のカメラで構築しますよ
camera = cv2.VideoCapture(0)

# カメラデバイスをオープンできなかったら例外吐いて死ぬ
if not camera.isOpened():
  raise Exception, "cannot open camera"

# カメラからエラー情報とセットで画像を読み取る
retval, image = camera.read()

# 画像の読み取りにエラーがあった場合は例外吐いて死ぬ
if not retval:
  raise Exception, "query frame failed"

# おまけ1: キャプチャーした画像をファイルとして保存
cv2.imwrite("image.jpg", 100)

# おまけ2: キャプチャーした画像をウィンドウ出して表示
window_name = "camera-sample"
cv2.namedWindow(window_name)
cv2.imshow(window_name, image)
# ウィンドウ上で任意のキーが押されるのを待ちます
# 注意: ウィンドウを☓で閉じたりすると pkill しないと終了しなくなります
cv2.waitKey(0)


# 参考:
#   - OpenCV-2.4.8.0 における画像とビデオの読み書き（英語・公式情報）
#     - http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html

