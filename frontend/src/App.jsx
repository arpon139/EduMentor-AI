import { useEffect, useState } from 'react'
import api from './api'

function App() {
  const [backend, setBackend] = useState('চেক করা হচ্ছে...')
  const [db, setDb] = useState('চেক করা হচ্ছে...')

  useEffect(() => {
    api.get('/')
      .then((res) => setBackend(res.data.message))
      .catch(() => setBackend('❌ Backend-এর সাথে কানেক্ট হয়নি'))

    api.get('/db-check')
      .then((res) => setDb(res.data.database))
      .catch(() => setDb('❌ Database কানেক্ট হয়নি'))
  }, [])

  return (
    <div className="min-h-screen flex items-center justify-center bg-slate-100">
      <div className="bg-white shadow-lg rounded-2xl p-8 w-96">
        <h1 className="text-2xl font-bold text-indigo-600 mb-4">EduMentor AI</h1>
        <p className="mb-2">Backend: <span className="font-semibold">{backend}</span></p>
        <p>Database: <span className="font-semibold">{db}</span></p>
      </div>
    </div>
  )
}

export default App