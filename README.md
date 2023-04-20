# Test task for SABER
Билд-система на FastAPI. Обеспечивает функционал получения списка задач по имени билда.

Файлы с билдами и задачами находятся в папке builds.

Инструкция по запуску:

Клонировать репозиторий:

`git clone git@github.com:MkhvDm/saber_task.git`

Находясь в директории saber_task, активировать виртуальное окружение:

```
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Тестирование и проверка линтером:
```
pytest
flake8 app 
```

Запуск:
```
python run.py
```

Enjoy!

### Примеры запроса:
1) POST: http://127.0.0.1:8000/get_tasks 
```
{
    "build": "test_build"
}
```
RESPONSE:
```
[
    "bring_gray_fairies",
    "build_white_fairies",
    "coloring_silver_fairies",
    "design_purple_fairies",
    "bring_aqua_leprechauns"
]
```
2) POST: http://127.0.0.1:8000/get_tasks 
```
{
    "build": "forward_interest"
}
```
RESPONSE:
```
[
    "build_teal_leprechauns",
    "coloring_aqua_centaurs",
    "bring_olive_centaurs",
    "enable_yellow_centaurs",
    "create_maroon_centaurs",
    "coloring_white_centaurs",
    "create_teal_centaurs",
    "design_lime_centaurs",
    "train_purple_centaurs",
    "upgrade_navy_centaurs",
    "create_olive_centaurs",
    "bring_blue_centaurs",
    "read_yellow_centaurs",
    "upgrade_navy_centaurs",
    "coloring_navy_golems",
    "coloring_aqua_golems",
    "enable_lime_leprechauns",
    "map_olive_leprechauns",
    "map_black_leprechauns",
    "upgrade_white_leprechauns",
    "enable_lime_leprechauns",
    "map_olive_leprechauns",
    "map_black_leprechauns",
    "upgrade_white_leprechauns",
    "enable_olive_humans",
    "create_aqua_humans",
    "enable_silver_humans",
    "create_purple_humans",
    "build_maroon_humans",
    "write_silver_humans",
    "write_white_humans",
    "train_white_humans",
    "write_teal_humans",
    "write_blue_ogres",
    "enable_fuchsia_ogres",
    "bring_blue_ogres",
    "design_white_ogres",
    "train_green_ogres",
    "upgrade_aqua_ogres",
    "write_silver_ogres",
    "upgrade_navy_ogres",
    "bring_green_ogres",
    "build_yellow_ogres",
    "create_maroon_ogres",
    "design_green_ogres",
    "write_fuchsia_golems"
]

### Авторы
Дмитрий Михеев - https://t.me/MkhvDm
