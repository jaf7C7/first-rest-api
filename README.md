# Rest APIs With Flask And Python

[Course home](https://www.udemy.com/course/rest-api-flask-and-python) \
[Instructor's code](https://github.com/tecladocode/rest-apis-flask-python) \
[Course e-book](https://rest-apis-flask.teclado.com/docs/course_intro/)


How to build and run the container to allow hot-reloading of the flask app:
```
img=$(podman build -t first-rest-api . | tail -1)
# `:z,ro` makes the mounted volume readable, but not writable, from the container
# See: `man -P 'less +"/Labeling Volume Mounts"' podman-run`
ctr=$(podman run -dp 5000:5000 -v .:/app:z,ro $img)
```
