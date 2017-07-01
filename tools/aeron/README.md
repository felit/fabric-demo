Aeron 提供高效可靠的单播和多播消息传输机制。

相关技术术语：

传输介质: 可通过UDP、InfiniBand、共享内存等

介质驱动: Driver for read/writing to/from transmission media for Aeron.

发布者: This is the client application which emits messages.

发送者: The media driver which sends the messages produced by the client publisher.

接收者: The media driver which receives messages send by the Sender.

订阅者: The client application which is receiving messages.

驱动订阅 Driver Subscription: The media driver in charge of message receipt. These messages are passed on to client Subscription applications.

会话 Session: A unique invocation of Aeron that identifies a single Publication and all Subscriptions for that Publication.

会话ID Session ID: A unique identifier for a Session.

频道 Channel: A transmission media needs to have a means of identifying a flow of data and the addressing model of the media. For Aeron, this is called a Channel. For different transmission media, the channel is defined differently. In general, a URI is used for specifying a channel.

物理来源 Physical Source: Source of a Session.

物理接收者 Physical Receiver: Receiver of a Session.

流 Stream: A Session carries sub-sessions within it. Streams are these sub-sessions.

流ID Stream ID: A unique identifier for a Stream. A value of 0 is reserved.

Term: A section of data within a Stream. Each Term is associated with a Media Driver send and receive buffer. The length of a Term must be a factor of two and must be the same length on both ends.

Term ID: A unique identifier for a Term within a Stream. Starts randomly. Must increase monotonically. Can wrap around. Can not go back to a wrapped value.

Term Offset: Identifier of a single byte within the Term. Always start at 0. This is the number of the byte within a given term starting from the beginning.

Frame: The unit of data for Aeron. Measured in bytes. The transmission media may include multiple Frames into a single packet of data for batching.

Message (aka APDU): The unit of data for the application. APDU means APplication Data Unit. A single Message may be fragmented over multiple Frames. Alternatively, a single Message may fit into a single Frame. A message, all of its fragments, must fit into a single Term.

Fragment: The unit of data for a fragmented Message that fits into a single Frame.

