import tensorflow.compat.v1 as tf
# import tensorflow as tf
import matplotlib.pyplot as plt
import io

def write_event(data, plotTitle="plotTitle"):
    '''
    params:
        data
        plotTitle
    '''
    def gen_plot(data, plotTitle):
        """Create a pyplot plot and save to buffer."""
        plt.figure()
        plt.plot(data)
        plt.title(plotTitle)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        return buf

    # Prepare the plot
    plot_buf = gen_plot(data, plotTitle)

    # Convert PNG buffer to TF image
    image = tf.image.decode_png(plot_buf.getvalue(), channels=4)

    # Add the batch dimension
    image = tf.expand_dims(image, 0)

    # Add image summary
    summary_op1 = tf.summary.image(plotTitle, image)
    #summary_op2 = tf.summary.text('tag1', tf.convert_to_tensor('Tag1: Random Text 1'))

    with tf.Session() as sess:
        summary = sess.run(summary_op1)
        writer = tf.summary.FileWriter('./logs')
        writer.add_summary(summary)
        writer.close()
        sess.close() # need to close session because next func call will use existing sess

    return