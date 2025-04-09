#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Использование: $0 <директория>"
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "Ошибка: Директория '$1' не существует."
    exit 1
fi

du -sh "$1"