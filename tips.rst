Sometimes I created a video, for example a Kazaam screencast, and Firefox will
not display the video with a message that says it is a corrupt file. Applying
this ``pix_fmt`` fixes it:

.. code-block:: bash

   ffmpeg -i corrupt-video.mp4 -pix_fmt yuv420p uncorrupted-video.mp4
