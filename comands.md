### comando utilizado para visualizar as imagens existentes:
```Bash
    Docker ps -a
```
### comando utilizado para iniciar um container:
```Bash
    Docker run container_name
```
### comando utilizado para construir uma imagem:
```Bash
    Docker build image_name <directory_path> | .
```
### comando utilizado para trocar porta de um container:
```Bash
    Docker run -p localport:container_port -d docker_image_name
```
### comando para remover um container 
```Bash
    Docker rm image_id
```
### comando para para um container 
```Bash
    Docker stop image_id
```
### comando para instalar imagens
```Bash
    Docker pull image_name
```
### comando para iniciar um container com mysql
```Bash
    Docker run --name <container_name> -e MYSQL_ROOT_PASSWORD=<passwd> -d mysql:tag
    EX: docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
```
**nesse comando a tag -e indica inserção de env e -d indica deteached para evitar travamentos no container. mysql:tag é utilizado para promover um versionamento do container** 
****
