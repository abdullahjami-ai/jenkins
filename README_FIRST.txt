===========================================================
  WEEK 18 - DAY 1 : DOCKER FUNDAMENTALS
===========================================================

  1. Unzip this folder somewhere simple, e.g.
        Windows :  C:\docker-class
        Linux   :  ~/docker-class

     (Do NOT work inside the zip file itself - Windows lets
      you browse a zip without unzipping, and nothing will
      work if you do that.)

  2. Double-click  START_HERE.html
     It opens in your browser. That page is the whole class:
     every command with a Copy button and an explanation.

  3. At the top of that page, choose Windows or Mac/Linux.
     The commands change depending on your system.

-----------------------------------------------------------
  WHAT IS IN THIS FOLDER
-----------------------------------------------------------

  START_HERE.html    <- open this. All commands, click to copy.
  project/           <- the small app we will containerise
      app.py            the FastAPI application
      requirements.txt  its Python dependencies
      Dockerfile        the recipe for building the image
      .dockerignore     files to keep out of the image
      whoami.py         a script for the volumes demo

  Week18_Day1_Docker_Fundamentals.pptx   the slides

-----------------------------------------------------------
  IF DOCKER IS NOT INSTALLED YET
-----------------------------------------------------------

  START_HERE.html has an install section, but Docker Desktop
  on Windows needs a reboot and a big download. If you have
  not installed it yet, use this in your browser instead so
  you can still follow along today:

        https://labs.play-with-docker.com
        (free, needs a free Docker Hub account)

===========================================================
