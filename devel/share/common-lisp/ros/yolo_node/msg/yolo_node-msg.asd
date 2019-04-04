
(cl:in-package :asdf)

(defsystem "yolo_node-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
    (:file "detection_info" :depends-on ("_package_detection_info"))
    (:file "_package_detection_info" :depends-on ("_package"))
  ))