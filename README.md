# 起動手順
## 0. gitkeepの削除
- data/dbに「.gitkeep」がある場合削除する
```
rm -f ./data/db/.gitkeep
```
## 1.Dockerコンテナ起動
```
$ docker compose up
```
## その他
- もしサーバーが起動していない場合、コンテナ内部で下記を実行する
```
$ docker exec -it [webのコンテナ名]  bash
# python manage.py runserver 0.0.0.0:8000
```

- コンテナに入って、管理者アカウントを作成する場合
```
$ docker exec -it [webのコンテナ名]  bash
# python manage.py createsuperuser
```

