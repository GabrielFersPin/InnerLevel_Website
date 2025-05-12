import React, { useState } from 'react'

function App() {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async () => {
    setLoading(true)
    setError(null)
    
    const task = {
      name: "Leer 20 minutos",
      points: 10,
      mood_before: "cansado",
      mood_after: "mejor"
    }

    try {
      const res = await fetch("http://localhost:8000/task", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(task)
      })

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`)
      }

      const data = await res.json()
      alert(data.message)
    } catch (err) {
      setError(err.message)
      alert(`Error: ${err.message}`)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="p-4 font-sans text-center">
      <h1 className="text-2xl font-bold text-green-600">RaízXP</h1>
      <button 
        className="mt-6 bg-green-500 text-white px-4 py-2 rounded disabled:opacity-50"
        onClick={handleSubmit}
        disabled={loading}>
        {loading ? 'Enviando...' : 'Enviar tarea de prueba'}
      </button>
      {error && (
        <p className="mt-4 text-red-500">{error}</p>
      )}
    </div>
  )
}

export default App 