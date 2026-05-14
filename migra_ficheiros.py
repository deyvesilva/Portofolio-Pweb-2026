import os
from django.conf import settings
from django.core.files import File
from portfolio.models import Tecnologia, UnidadeCurricular, Projeto, MakingOf
from artigos.models import Artigo
from escola.models import Curso

def migrar_campo(Modelo, nome_campo):
    print(f"\n>>> A verificar {Modelo.__name__} (campo: {nome_campo})...")
    count = 0
    
    # Onde os ficheiros estão realmente (Pasta media na raiz do projeto)
    media_local_root = os.path.join(settings.BASE_DIR, 'media')

    for obj in Modelo.objects.all():
        campo = getattr(obj, nome_campo)
        
        # Se o objeto tem um nome de ficheiro registado (ex: "projetos/foto.png")
        if campo and campo.name:
            try:
                # CONSTRUÇÃO MANUAL DO CAMINHO:
                # Pegamos no nome que está na BD e juntamos à pasta media local
                nome_ficheiro = campo.name
                local_path = os.path.join(media_local_root, nome_ficheiro)
                
                if os.path.exists(local_path):
                    with open(local_path, 'rb') as f:
                        # O save() vai enviar para o Cloudinary
                        campo.save(
                            os.path.basename(local_path),
                            File(f),
                            save=True
                        )
                    print(f"  [OK] Migrado com sucesso: {obj}")
                    count += 1
                else:
                    print(f"  [AVISO] Ficheiro não encontrado no disco: {local_path}")
            except Exception as e:
                print(f"  [ERRO] Falha ao migrar {obj}: {e}")
    
    print(f"--- Total de {Modelo.__name__} migrados: {count} ---")

def executar_migracao_total():
    # 1. App Portfolio
    migrar_campo(Tecnologia, 'logo')
    migrar_campo(UnidadeCurricular, 'imagem')
    migrar_campo(Projeto, 'logo')
    migrar_campo(MakingOf, 'registos')
    
    # 2. App Artigos
    migrar_campo(Artigo, 'fotografia')
    
    # 3. App Escola
    migrar_campo(Curso, 'imagem')

    print("\n✅ Processo concluído!")