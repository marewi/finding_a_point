import io

import matplotlib.pyplot as plt
import tensorflow as tf

from lib.toStringExt import paremetersToString


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
    summary = tf.summary.image(plotTitle, image)
    # summary_op = tf.compat.v1.summary.text("greeting", "test")

    return(summary)
