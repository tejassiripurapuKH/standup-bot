#!/bin/sh
TAG="${1}"

if [ $TAG ]
then
  docker build -t tejassiripurapu/standup-bot:${TAG} -t tejassiripurapu/standup-bot:latest .
else
  docker build -t tejassiripurapu/standup-bot:latest .
fi

docker push tejassiripurapu/standup-bot

# update deployment with latest image
kubectl config use-context dev-eks1
kubectl rollout restart deploy standup-bot-deployment -n tejas
