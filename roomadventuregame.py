import streamlit as st
  
room = {
    'entrance':{'north':'hall','east':'kitchen'},
    'hall':{'south':'entrance','east':'bedroom'},
    'kitchen':{'west':'entrance','north':'bedroom'},
    'bedroom':{'west':'hall','south':'kitchen'}
 }

if "current_room" not in st.session_state:
    st.session_state.current_room = "entrance"

def move(direction):
    try:
        if direction not in room[st.session_state.current_room]:
            raise ValueError("You cant move in that direction")
        st.session_state.current_room = room[(st.session_state.current_room)][direction]
    except ValueError as ve: 
        st.error(ve)
    except Exception as e:
        st.error(f"An unexpected error has occurred {e}")
    else:
        st.success(f"you have opted to move to the {direction} direction you are now in the {st.session_state.current_room}")

    finally:
         st.write(f"your current room is {st.session_state.current_room}")


        

direction = st.text_input("Enter a direction north,south,east, or west")
if st.button("Move"):
    move(direction)



    

