from app import create_app
from modules import thread_collectData


app = create_app()

if __name__ == '__main__':
    thread_collectData.start_background_task()
    app.run(debug=False, host='0.0.0.0', port=5000)
