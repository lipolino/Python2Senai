nomeCurso = "Programação em Python"
cargaHoraria = 60
media = 8.5
status = True

print(f"""
--- Informações do Curso ---
Nome do curso: {nomeCurso} {type(nomeCurso)}

--- Detalhes Numéricos ---
Carga Horária Total (horas): {cargaHoraria} {type(cargaHoraria)}
Nota Média Esperada: {media} {type(media)}

--- Status do Curso ---
O curso já foi iniciado? {status} {type(status)}

--- Informações gerais do curso: ---

Resumo:
O curso {nomeCurso} tem nota média esperada 8.5
Status de início: {status}.
Carga Horária: {cargaHoraria}.

--- Fim do Programa ---""")