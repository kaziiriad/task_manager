# Task Manager

### A web based task management application based on python's django framework.

### Project is live [here](https://honest-behavior-production.up.railway.app/)

## Build Guide

1. Clone the repository

```bash
git clone https://github.com/kaziiriad/task_manager.git/
cd task_manager/
```

2. Add variables to the ```.env``` file

3. Run with ```docker-compose```

```bash
docker-compose run web python manage.py migrate
docker-compose up
```
4. Visit ```https://localhost:8000``` to open the app.