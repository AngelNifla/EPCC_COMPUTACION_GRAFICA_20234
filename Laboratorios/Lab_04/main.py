import cv2
import mediapipe as mp
import numpy as np

########## Inicializar MediaPipe Pose. ####################
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def Calcular_Angulo(a_, b_, c_):        # Función para calcular el ángulo entre tres puntos.
    a_ = np.array(a_)  # Punto A
    b_ = np.array(b_)  # (vértice)
    c_ = np.array(c_)  # Punto B
    
    A = np.arctan2(c_[1] - b_[1], c_[0] - b_[0])
    B = np.arctan2(a_[1] - b_[1], a_[0] - b_[0])
    Radianes = A - B
    Angulo = np.abs(Radianes * 180.0 / np.pi)
    
    if Angulo > 180.0:
        Angulo = 360 - Angulo
        
    return Angulo

################## Funciones de ejercicios ########################
def SENTADILLA(PuntosRefer):
    cadera = [PuntosRefer[mp_pose.PoseLandmark.LEFT_HIP.value].x,
           PuntosRefer[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    rodilla = [PuntosRefer[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
            PuntosRefer[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    tobillo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
             PuntosRefer[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
    hombro = [PuntosRefer[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
             PuntosRefer[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    
    angulo_rodilla = Calcular_Angulo(cadera, rodilla, tobillo)
    angulo_cadera = Calcular_Angulo(hombro, cadera, rodilla)
    
    return angulo_rodilla < 90 and angulo_cadera < 90

def POLICHINELAS(PuntosRefer):###################
    hombro_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                     PuntosRefer[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    cadera_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                PuntosRefer[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    tobillo_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                 PuntosRefer[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

    codo_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                 PuntosRefer[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    
    angulo_cadera_izquierdo = Calcular_Angulo(hombro_izquierdo, cadera_izquierdo, tobillo_izquierdo)
    angulo_hombro_izquierdo = Calcular_Angulo(cadera_izquierdo, hombro_izquierdo, codo_izquierdo)
    return (100 < angulo_cadera_izquierdo < 170 )and (90 < angulo_hombro_izquierdo)

def PLANCHA(PuntosRefer):
    hombro_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                     PuntosRefer[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
    cadera_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                PuntosRefer[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    tobillo_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                  PuntosRefer[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    codo_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                PuntosRefer[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
    muñeca_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                  PuntosRefer[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

    angulo_cuerpo = Calcular_Angulo(hombro_izquierdo, cadera_izquierdo, tobillo_izquierdo)
    angulo_brazo = Calcular_Angulo(hombro_izquierdo, codo_izquierdo, muñeca_izquierdo)

    return 170 < angulo_cuerpo < 195 and angulo_brazo < 90

def ESTOCADA(PuntosRefer):
    rodilla_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                 PuntosRefer[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
    cadera_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                PuntosRefer[mp_pose.PoseLandmark.LEFT_HIP.value].y]
    tobillo_izquierdo = [PuntosRefer[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                  PuntosRefer[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

    rodilla_derecho = [PuntosRefer[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                 PuntosRefer[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
    cadera_derecho = [PuntosRefer[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                PuntosRefer[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
    tobillo_derecho = [PuntosRefer[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                  PuntosRefer[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
    
    angulo_rodilla_izquierdo = Calcular_Angulo(cadera_izquierdo, rodilla_izquierdo, tobillo_izquierdo)
    angulo_rodilla_derecho = Calcular_Angulo(cadera_derecho, rodilla_derecho, tobillo_derecho)

    angulo_tobillos_rodilla_izq = Calcular_Angulo(tobillo_izquierdo, rodilla_izquierdo, tobillo_derecho)
    angulo_tobillos_rodilla_der = Calcular_Angulo(tobillo_izquierdo, rodilla_derecho, tobillo_derecho)

    angulo_tobillos_rodilla = ((130 < angulo_tobillos_rodilla_der < 180)or(130 < angulo_tobillos_rodilla_izq < 180))
    
    return (angulo_rodilla_derecho < 90 and angulo_rodilla_izquierdo < 90)# and angulo_tobillos_rodilla

############# Función de verificación ############
def VERIFICAR(cap, Ejercicio):
    exercise_counter = 0
    exercise_position = None
    
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                break

            height, width, _ = frame.shape##
            frame = cv2.flip(frame, 1)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            try:
                PuntosRefer = results.pose_landmarks.landmark
                
                if Ejercicio == '1':                                     ####Sentadilla
                    correct_position = SENTADILLA(PuntosRefer)
                    Ejercicio_nombre = 'SENTADILLAS'
                    label = 'Sentadilla Correcta' if correct_position else 'Baje mas'
                elif Ejercicio == '2':                                     ####Polichinela
                    correct_position = POLICHINELAS(PuntosRefer)
                    Ejercicio_nombre = 'POLICHINELAS'
                    label = 'Polichinela Correcta' if correct_position else 'Separe mas'
                elif Ejercicio == '3':                                     ####Plancha
                    correct_position = PLANCHA(PuntosRefer)
                    Ejercicio_nombre = 'PLANCHAS'
                    label = 'Plancha Correcta' if correct_position else 'Ajuste el cuerpo'
                elif Ejercicio == '4':                                     ####Walking_Lunge
                    correct_position = ESTOCADA(PuntosRefer)
                    Ejercicio_nombre = 'ESTOCADAS'
                    label = 'Lunge Correcta' if correct_position else 'Baje mas'
                else:
                    correct_position = False
                    label = 'Ejercicio no válido'
                
                if correct_position:
                    if exercise_position != "down":
                        exercise_counter += 1
                        exercise_position = "down"
                else:
                    exercise_position = "up"
                
                cv2.putText(image, f'{label}', (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if correct_position else (0, 0, 255), 2, cv2.LINE_4)
                cv2.putText(image, f'{Ejercicio_nombre.capitalize()}: {exercise_counter}', (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                
            except:
                pass
            

            ############## Se muestran los puntos necesarios ##################
            if results.pose_landmarks is not None:
                x1 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width)
                y1 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height)

                x2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * width)
                y2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * height)

                x3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * width)
                y3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * height)

                x4 = int(results.pose_landmarks.landmark[11].x * width)
                y4 = int(results.pose_landmarks.landmark[11].y * height)

                x5 = int(results.pose_landmarks.landmark[13].x * width)
                y5 = int(results.pose_landmarks.landmark[13].y * height)

                x6 = int(results.pose_landmarks.landmark[15].x * width)
                y6 = int(results.pose_landmarks.landmark[15].y * height)



                x7 = int(results.pose_landmarks.landmark[24].x * width)
                y7 = int(results.pose_landmarks.landmark[24].y * height)

                x8 = int(results.pose_landmarks.landmark[26].x * width)
                y8 = int(results.pose_landmarks.landmark[26].y * height)

                x9 = int(results.pose_landmarks.landmark[28].x * width)
                y9 = int(results.pose_landmarks.landmark[28].y * height)



                x10 = int(results.pose_landmarks.landmark[23].x * width)
                y10 = int(results.pose_landmarks.landmark[23].y * height)

                x11 = int(results.pose_landmarks.landmark[25].x * width)
                y11 = int(results.pose_landmarks.landmark[25].y * height)

                x12 = int(results.pose_landmarks.landmark[27].x * width)
                y12 = int(results.pose_landmarks.landmark[27].y * height)



                ############## Se dibujan los puntos ########################
                cv2.line(image, (x3, y3), (x2, y2), (255, 255, 255), 3)
                cv2.line(image, (x2, y2), (x1, y1), (255, 255, 255), 3)
                cv2.line(image, (x1, y1), (x7, y7), (255, 255, 255), 3)
                cv2.line(image, (x7, y7), (x8, y8), (255, 255, 255), 3)
                cv2.line(image, (x8, y8), (x9, y9), (255, 255, 255), 3)
                cv2.circle(image, (x1, y1), 6, (128, 0, 255), -1)
                cv2.circle(image, (x2, y2), 6, (128, 0, 255), -1)
                cv2.circle(image, (x3, y3), 6, (128, 0, 255), -1)
                cv2.circle(image, (x7, y7), 6, (128, 0, 255), -1)
                cv2.circle(image, (x8, y8), 6, (128, 0, 255), -1)
                cv2.circle(image, (x9, y9), 6, (128, 0, 255), -1)

                cv2.line(image, (x6, y6), (x5, y5), (255, 255, 255), 3)
                cv2.line(image, (x5, y5), (x4, y4), (255, 255, 255), 3)
                cv2.line(image, (x4, y4), (x10, y10), (255, 255, 255), 3)
                cv2.line(image, (x10, y10), (x11, y11), (255, 255, 255), 3)
                cv2.line(image, (x11, y11), (x12, y12), (255, 255, 255), 3)
                cv2.circle(image, (x4, y4), 6, (255, 191, 0), -1)
                cv2.circle(image, (x5, y5), 6, (255, 191, 0), -1)
                cv2.circle(image, (x6, y6), 6, (255, 191, 0), -1)
                cv2.circle(image, (x10, y10), 6, (255, 191, 0), -1)
                cv2.circle(image, (x11, y11), 6, (255, 191, 0), -1)
                cv2.circle(image, (x12, y12), 6, (255, 191, 0), -1)

            ############# Se muestran todos los 33  puntos ###########
            #mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            #                          landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
            #                          connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))
                
            cv2.imshow('Ejercicio', image)
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

########### Función principal ###########################
def main():
    Ejercicio = input("Ingrese el ejercicio a verificar:\n--Sentadilla[1]\n--polichinela[2]\n--plancha[3]\n--Estocada[4]\nIngrese Opcion: ").strip().lower()
    opcion = input("¿Desea usar la cámara (c) o abrir un video (v)? ").strip().lower()
    
    if opcion == 'c':
        cap = cv2.VideoCapture(0)
    elif opcion == 'v':
        video_path = input("Ingrese la ruta del video: ").strip()
        cap = cv2.VideoCapture(video_path)
    else:
        print("Opción no válida. Saliendo...")
        return
    
    VERIFICAR(cap, Ejercicio)

if __name__ == "__main__":
    main()
