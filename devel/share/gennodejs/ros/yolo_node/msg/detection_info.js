// Auto-generated. Do not edit!

// (in-package yolo_node.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class detection_info {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.class_type = null;
      this.score = null;
      this.x1 = null;
      this.x2 = null;
      this.y1 = null;
      this.y2 = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('class_type')) {
        this.class_type = initObj.class_type
      }
      else {
        this.class_type = [];
      }
      if (initObj.hasOwnProperty('score')) {
        this.score = initObj.score
      }
      else {
        this.score = [];
      }
      if (initObj.hasOwnProperty('x1')) {
        this.x1 = initObj.x1
      }
      else {
        this.x1 = [];
      }
      if (initObj.hasOwnProperty('x2')) {
        this.x2 = initObj.x2
      }
      else {
        this.x2 = [];
      }
      if (initObj.hasOwnProperty('y1')) {
        this.y1 = initObj.y1
      }
      else {
        this.y1 = [];
      }
      if (initObj.hasOwnProperty('y2')) {
        this.y2 = initObj.y2
      }
      else {
        this.y2 = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type detection_info
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [class_type]
    bufferOffset = _arraySerializer.string(obj.class_type, buffer, bufferOffset, null);
    // Serialize message field [score]
    bufferOffset = _arraySerializer.float32(obj.score, buffer, bufferOffset, null);
    // Serialize message field [x1]
    bufferOffset = _arraySerializer.int16(obj.x1, buffer, bufferOffset, null);
    // Serialize message field [x2]
    bufferOffset = _arraySerializer.int16(obj.x2, buffer, bufferOffset, null);
    // Serialize message field [y1]
    bufferOffset = _arraySerializer.int16(obj.y1, buffer, bufferOffset, null);
    // Serialize message field [y2]
    bufferOffset = _arraySerializer.int16(obj.y2, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type detection_info
    let len;
    let data = new detection_info(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [class_type]
    data.class_type = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [score]
    data.score = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [x1]
    data.x1 = _arrayDeserializer.int16(buffer, bufferOffset, null)
    // Deserialize message field [x2]
    data.x2 = _arrayDeserializer.int16(buffer, bufferOffset, null)
    // Deserialize message field [y1]
    data.y1 = _arrayDeserializer.int16(buffer, bufferOffset, null)
    // Deserialize message field [y2]
    data.y2 = _arrayDeserializer.int16(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.class_type.forEach((val) => {
      length += 4 + val.length;
    });
    length += 4 * object.score.length;
    length += 2 * object.x1.length;
    length += 2 * object.x2.length;
    length += 2 * object.y1.length;
    length += 2 * object.y2.length;
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'yolo_node/detection_info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ea2d9911aca1cdbc2e7d80a7846b80e6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    string[] class_type
    float32[] score
    int16[] x1
    int16[] x2
    int16[] y1
    int16[] y2
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new detection_info(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.class_type !== undefined) {
      resolved.class_type = msg.class_type;
    }
    else {
      resolved.class_type = []
    }

    if (msg.score !== undefined) {
      resolved.score = msg.score;
    }
    else {
      resolved.score = []
    }

    if (msg.x1 !== undefined) {
      resolved.x1 = msg.x1;
    }
    else {
      resolved.x1 = []
    }

    if (msg.x2 !== undefined) {
      resolved.x2 = msg.x2;
    }
    else {
      resolved.x2 = []
    }

    if (msg.y1 !== undefined) {
      resolved.y1 = msg.y1;
    }
    else {
      resolved.y1 = []
    }

    if (msg.y2 !== undefined) {
      resolved.y2 = msg.y2;
    }
    else {
      resolved.y2 = []
    }

    return resolved;
    }
};

module.exports = detection_info;
