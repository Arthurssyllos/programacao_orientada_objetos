from classes.menuGerenciadorS3 import MenuGerenciadorS3

nome_bucket = "aulanoitearthur"

menu = MenuGerenciadorS3(nome_bucket)

menu.executar()

#controla_s3 = GerenciarS3('aulanoitearthur')

#controla_s3.lista_arquivos()

#controla_s3.delete_arquivo()

#controla_s3.upload_arquivo('/home/ec2-user/environment/programacao_orientada_objetos/arquivos/index.html', 'index.html')

#diretorio_destino = '/home/ec2-user/environment/programacao_orientada_objetos/arquivos'

#nome_arquivo = 'index.html'

#controla_s3.download_arquivo(nome_arquivo, diretorio_destino)