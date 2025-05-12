import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold text-gray-900">InnerLevel</h1>
          <p className="mt-1 text-sm text-gray-600">Your Personal Growth Journey</p>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Tasks Card */}
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Today's Tasks</h2>
            <div className="space-y-4">
              <div className="flex items-center justify-between p-3 bg-blue-50 rounded">
                <span className="text-gray-700">Complete project proposal</span>
                <span className="text-sm text-blue-600">+10 points</span>
              </div>
              <div className="flex items-center justify-between p-3 bg-green-50 rounded">
                <span className="text-gray-700">Morning meditation</span>
                <span className="text-sm text-green-600">+5 points</span>
              </div>
            </div>
          </div>

          {/* Progress Card */}
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Your Progress</h2>
            <div className="space-y-4">
              <div className="flex justify-between items-center">
                <span className="text-gray-600">Level</span>
                <span className="text-lg font-bold text-blue-600">3</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2.5">
                <div className="bg-blue-600 h-2.5 rounded-full" style={{ width: '45%' }}></div>
              </div>
              <p className="text-sm text-gray-500">450/1000 points to next level</p>
            </div>
          </div>

          {/* Mood Tracker Card */}
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Mood Tracker</h2>
            <div className="grid grid-cols-5 gap-2">
              {['😊', '😐', '😌', '😔', '😡'].map((emoji, index) => (
                <button
                  key={index}
                  className="text-2xl p-2 hover:bg-gray-100 rounded transition-colors"
                  onClick={() => console.log(`Selected mood: ${emoji}`)}
                >
                  {emoji}
                </button>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  )
}

export default App
