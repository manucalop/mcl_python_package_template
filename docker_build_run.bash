#!/usr/bin/env bash
pkg_name="python_package_template"

echo "Buiding container..."
docker image build -t $pkg_name .

echo "Running..."
docker run -p 3000:3000 --name $pkg_name -t $pkg_name

echo "Deleting container..."
docker rm $pkg_name
