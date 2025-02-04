Sometimes I created a video, for example a Kazaam screencast, and Firefox will
not display the video with a message that says it is a corrupt file. Applying
this ``pix_fmt`` fixes it:

.. code-block:: bash

   ffmpeg -i corrupt-video.mp4 -pix_fmt yuv420p uncorrupted-video.mp4


Convert first page of PDF to image file.

.. code-block:: bash

   convert -density 150 -trim Biorob.pdf[0] -quality 100 -flatten -sharpen 0x1.0 leila-biorob.png

Mount an S3 bucket

Install ``sudo apt install s3fs``.

Create ``~/.passwd-s3fs`` with one line ``ACCESS_KEY_ID:SECRETE_ACCESS_KEY``

Create a directory ``dreamobject-bucket`` and then mount with:

.. code-block:: bash

   s3fs BUCKET_NAME dreamobject-bucket/ -o passwd_file=~/.passwd-s3fs -o url=https://objects-us-east-1.dream.io

How to deal with Vim swp files
==============================

From: https://vim.fandom.com/wiki/Swap_file_%22...%22already_exists!_-_so_diff_it

- `r # at the prompt hit "r" to recover the swap file`
- `:sav! /tmp/%`
- `:vs`
- `:diffthis`
- `CTRL-W_l`
- `:bp`
- `e # at the prompt hit "e" to edit anyway`
- `:diffthis`
