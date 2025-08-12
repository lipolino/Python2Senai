var_nome_aluno = input('Digite o nome do Aluno: ')
var_nota1_aluno = float(input('Digite a nota do primeiro bimestre: '))
var_nota2_aluno = float(input('Digite a nota do segundo bimestre: '))
var_nota3_aluno = float(input('Digite a nota do terceiro bimestre: '))
var_nota4_aluno = float(input('Digite a nota do quarto bimestre: '))

var_media_aluno = (var_nota1_aluno + var_nota2_aluno + var_nota3_aluno + var_nota4_aluno) / 4

print(f"""
-------- BOLETIM DE NOTAS --------
Nome do Aluno(a): {var_nome_aluno}
Nota 1º bimestre: {var_nota1_aluno:.1f}
Nota 2º bimestre: {var_nota2_aluno:.1f}
Nota 3º bimestre: {var_nota3_aluno:.1f}
Nota 4º bimestre: {var_nota4_aluno:.1f}
Média Final: {var_media_aluno:.1f}
----------------------------------""")

              