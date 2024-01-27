import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import { Dashboard, Details, Home } from './screens'

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path='*' element={<Home />}></Route>
        <Route path='/' element={<Home />}></Route>
        <Route path='/dashboard' element={<Dashboard />}></Route>
        <Route path='/details' element={<Details />}></Route>
      </Routes>
    </Router>
  )
}

export default App
