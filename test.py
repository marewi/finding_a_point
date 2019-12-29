import matplotlib.pyplot as plt
import numpy
from model_table import Model_table
import tensorflow as tf

qtable = Model_table()

x = numpy.arange(0, 1, 0.05)
y = numpy.power(x, 2)

fig = plt.figure()
ax = fig.gca()
ax.set_xticks(numpy.arange(0, 1, 0.1))
ax.set_yticks(numpy.arange(0, 1., 0.1))
plt.scatter(x, y)
plt.grid()

with tf.Session() as sess:
    summary = sess.run(fig)
    writer = tf.summary.FileWriter('./test')
    writer.add_summary(summary)
    writer.close()
sess.close()

############

# plt.figure()
# plt.plot(data)
# plt.title(plotTitle)
# buf = io.BytesIO()
# plt.savefig(buf, format='png')
# buf.seek(0)
