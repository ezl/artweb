#!/bin/bash
####
#  API ECS Task Definition Template
#  Used By CI/CD
####

cat > ecs-deploy-task.json <<EOF
{
    "family":"artweb-api",
    "containerDefinitions":[
    {
      "volumesFrom": [],
      "memory": 1500,
      "portMappings": [
        {
          "hostPort": 0,
          "containerPort": 8000,
          "protocol": "tcp"
        }
      ],
      "essential": true,
      "entryPoint": [],
      "mountPoints": [],
      "name": "artweb-api",
      "environment": [
        {
          "name": "DJANGO_DEBUG",
          "value": "$DJANGO_DEBUG"
        },
        {
          "name": "DJANGO_SECRET_KEY",
          "value": "$DJANGO_SECRET_KEY"
        },
        {
          "name": "DATABASE_URL",
          "value": "$DATABASE_URL"
        }
      ],
      "links": [],
      "image": "$ECR_IMAGE",
      "command": [
        "sh",
        "-c",
        "python manage.py migrate && uwsgi --ini /app/uwsgi.ini"
      ],
      "logConfiguration": {
         "logDriver": "awslogs",
         "options": {
             "awslogs-group": "/ecs/artweb-api",
             "awslogs-region": "us-east-1",
             "awslogs-stream-prefix": "$AWSLOGS_STREAM_PREFIX",
             "awslogs-create-group": "true"
         }
      }
    }
  ]
}
EOF
