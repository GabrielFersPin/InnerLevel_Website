import React from 'react'
import ReactDOM from 'react-dom/client'

function App() {
  const handleSubmit = async () => {
    const task = {
      name: "Leer 20 minutos",
      points: 10,
      mood_before: "cansado",
      mood_after: "mejor"
    }

    const res = await fetch("http://localhost:8000/task", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(task)
    })

    const data = await res.json()
    alert(data.status)
  }

  return (
    <div className="p-4 font-sans text-center">
      <h1 className="text-2xl font-bold text-green-600">RaízXP</h1>
      <button 
        className="mt-6 bg-green-500 text-white px-4 py-2 rounded"
        onClick={handleSubmit}>
        Enviar tarea de prueba
      </button>
    </div>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
