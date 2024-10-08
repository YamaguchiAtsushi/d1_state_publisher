# import rclpy
# from rclpy.node import Node
# from geometry_msgs.msg import Pose
# from tsukutsuku2_msgs.msg import D1  # D1メッセージをインポート

# class D1WaypointPublisher(Node):

#     def __init__(self):
#         super().__init__('d1_msg_publisher')

#         # パブリッシャーの初期化
#         self.publisher = self.create_publisher(D1, 'd1_messages', 10)

#         # 一定間隔でパブリッシュするタイマーを設定（1秒ごと）
#         self.timer = self.create_timer(1.0, self.publish_messages)
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from tsukutsuku2_msgs.msg import D1  # D1メッセージをインポート

class D1WaypointPublisher(Node):

    def __init__(self):
        super().__init__('d1_msg_publisher')

        # パブリッシャーの初期化
        self.publisher = self.create_publisher(D1, 'd1_messages', 10)

        # 一定間隔でパブリッシュするタイマーを設定（1秒ごと）
        self.timer = self.create_timer(1.0, self.publish_messages)

    def publish_messages(self):
        # D1 メッセージを作成
        d1_msg = D1()

        # 各フィールドに値を設定
        d1_msg.character = 'a'  # ダミーデータ
        d1_msg.find_box = True  # ダミーデータ
        d1_msg.find_character = True  # ダミーデータ
        d1_msg.pose = Pose()
        d1_msg.pose.position.x = 1.0
        d1_msg.pose.position.y = 2.0
        d1_msg.pose.position.z = 0.0

        # メッセージをパブリッシュ
        self.publisher.publish(d1_msg)

        # ログに出力
        self.get_logger().info(f'Published D1 message: character={d1_msg.character}, '
                                f'find_box={d1_msg.find_box}, '
                                f'find_character={d1_msg.find_character}, '
                                f'position=({d1_msg.pose.position.x}, {d1_msg.pose.position.y}, {d1_msg.pose.position.z})')

def main(args=None):
    rclpy.init(args=args)
    node = D1WaypointPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    def publish_messages(self):
        # D1 メッセージを作成
        d1_msg = D1()

        # 各フィールドに値を設定
        d1_msg.character = 'a'  # ダミーデータ
        d1_msg.find_box = True  # ダミーデータ
        d1_msg.find_character = True  # ダミーデータ
        d1_msg.pose = Pose()
        d1_msg.pose.position.x = 1.0
        d1_msg.pose.position.y = 2.0
        d1_msg.pose.position.z = 0.0

        # メッセージをパブリッシュ
        self.publisher.publish(d1_msg)

        # ログに出力
        self.get_logger().info(f'Published D1 message: character={d1_msg.character}, '
                                f'find_box={d1_msg.find_box}, '
                                f'find_character={d1_msg.find_character}, '
                                f'position=({d1_msg.pose.position.x}, {d1_msg.pose.position.y}, {d1_msg.pose.position.z})')

def main(args=None):
    rclpy.init(args=args)
    node = D1WaypointPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()