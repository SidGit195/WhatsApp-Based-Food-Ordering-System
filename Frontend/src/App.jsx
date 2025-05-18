import { NavLink, Routes, Route } from 'react-router-dom'
import MenuPage from './components/Menu'
import OrdersPage from './components/Orders'

export default function App(){
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white py-6 mb-8">
        <h1 className="text-3xl font-bold text-center">
          Welcome to WhatsApp-Based Food Ordering System
        </h1>
      </header>
      <div className="max-w-5xl mx-auto px-4">
        <nav className="flex justify-center space-x-4 mb-6">
          <NavLink 
            to="/menu" 
            className={({isActive})=>
              `px-4 py-2 rounded font-medium ${
                isActive ? 'bg-blue-600 text-white' : 'bg-white text-blue-600 shadow'
              }`
            }
          >
            Menu
          </NavLink>
          <NavLink 
            to="/orders" 
            className={({isActive})=>
              `px-4 py-2 rounded font-medium ${
                isActive ? 'bg-green-600 text-white' : 'bg-white text-green-600 shadow'
              }`
            }
          >
            Orders
          </NavLink>
        </nav>
        <Routes>
          <Route path="/menu" element={<MenuPage/>}/>
          <Route path="/orders" element={<OrdersPage/>}/>
        </Routes>
      </div>
    </div>
  )
}