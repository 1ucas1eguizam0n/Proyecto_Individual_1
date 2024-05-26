from fastapi import FastAPI
import pandas as pd
import pickle
from Funciones.funcion_main import developer_info, developer_of_year, user_for_genre, user_info, review_developer

app = FastAPI()

with open('Modelos/Relaciones_muestra.pkl', 'rb') as file:
    model = pickle.load(file)

try:
    modelo = pd.read_parquet('Datos varios/relacionamiento_muestra.parquet', engine='fastparquet')
except Exception as e:
    print(f"Error reading parquet file with fastparquet: {e}")

@app.get('/')
async def inicio():
    return 'Nada que ver aqui...'

@app.get('/developer/{desarrollador}')
async def desarrollador_info(desarrollador: str):
    try:
        respuesta=developer_info(desarrollador)
        return respuesta.to_dict(orient="records")
    except Exception as e:
        return {f'Error: {str(e)}'}
    
@app.get('/User_data/{user_id}')
async def usuario_info(user_id: str):
    try:
        respuesta=user_info(user_id)
        return respuesta
    except Exception as e:
        return {f'Error: {str(e)}'}
    
@app.get('/Game_genre/{gen}')
async def usuario_mayor_tiempo(gen: str):
    try:
        respuesta=user_for_genre(gen)
        return respuesta
    except Exception as e:
        return {f'Error: {str(e)}'}
    
@app.get('/Best_developer/{anio}')
async def mejor_desarrollador(anio:int):
    try:
        respuesta=developer_of_year(anio)
        return respuesta.to_dict(orient="records")
    except Exception as e:
        return {f'Error: {str(e)}'}
    
@app.get('/developer_reviews/{dev}')
async def reviews_desarrollador(dev:str):
    try:
        respuesta=review_developer(dev)
        return respuesta.to_dict(orient='records')
    except Exception as e:
        return {f'Error: {str(e)}'}
    
@app.get('/recommend_games/{user_id}')
async def recomendacion(user_id:str):
    try:
        if user_id not in modelo['user_id'].unique():
            juegos_aleatorios=list(modelo['title'].sample(5))
            mensaje=f'El usuario {user_id} no posee ningún item en su biblioteca, por lo que la recomendación será aleatoria.'
            return {mensaje: juegos_aleatorios}
        else:
            diccionario={}
            juegos_valorados=modelo[modelo['user_id']==user_id]['title'].unique()
            todos_los_juegos=modelo['title'].unique()
            juegos_no_valorados=list(set(todos_los_juegos) - set(juegos_valorados))
            predicciones=[model.predict(user_id, juego) for juego in juegos_no_valorados]
            recomendaciones=sorted(predicciones, key=lambda x: x.est, reverse=True)[:5] 
            cont=1
            for recomendacion in recomendaciones:
                diccionario[f'Top {cont}']=recomendacion.iid
                cont +=1
        return {f'Usuario: {user_id}': diccionario}
    except Exception as e:
        return {f'Error: {str(e)}'}
