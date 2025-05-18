import { useState, useEffect } from 'react'
import { fetchMenu, addMenu } from '../services/api'

export default function MenuPage(){
  const [list, setList] = useState([])
  const [form, setForm] = useState({name:'',description:'',price:0,available:true})
  const [msg, setMsg] = useState('')

  useEffect(()=>{load()},[])
  async function load(){
    setList(await fetchMenu())
  }
  async function onSubmit(e){
    e.preventDefault()
    try{
      await addMenu(form)
      setMsg('Item added successfully')
      setForm({name:'',description:'',price:0,available:true})
      load()
    }catch{
      setMsg('Error adding item')
    }
    setTimeout(()=>setMsg(''),3000)
  }

  return (
    <div>
      <div className="bg-white shadow rounded-lg p-6 mb-8">
        <h2 className="text-2xl font-semibold mb-4">Menu Management</h2>
        {msg && <p className="mb-4 text-green-600">{msg}</p>}
        <form onSubmit={onSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <input required placeholder="Name"
            value={form.name}
            onChange={e=>setForm({...form, name:e.target.value})}
            className="border rounded p-2 w-full"
          />
          <input placeholder="Description"
            value={form.description}
            onChange={e=>setForm({...form, description:e.target.value})}
            className="border rounded p-2 w-full"
          />
          <input type="number" placeholder="Price"
            value={form.price}
            onChange={e=>setForm({...form, price:+e.target.value})}
            className="border rounded p-2 w-full"
          />
          <label className="flex items-center space-x-2">
            <input type="checkbox"
              checked={form.available}
              onChange={e=>setForm({...form, available:e.target.checked})}
              className="h-5 w-5 text-blue-600"
            />
            <span className="font-medium">Available</span>
          </label>
          <button type="submit" className="md:col-span-2 bg-blue-600 text-white rounded p-2 font-medium hover:bg-blue-700">
            {form.id ? 'Update Item' : 'Add Item'}
          </button>
        </form>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        {list.map(i=>(
          <div key={i.id} className="bg-white shadow rounded-lg p-4 flex justify-between items-center">
            <div>
              <h3 className="text-lg font-semibold">{i.name}</h3>
              <p className="text-sm text-gray-600">{i.description}</p>
              <p className="mt-1 font-medium">${i.price.toFixed(2)}</p>
            </div>
            <span className={`px-3 py-1 rounded-full text-sm ${
              i.available ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
            }`}>
              {i.available ? 'Available' : 'Unavailable'}
            </span>
          </div>
        ))}
      </div>
    </div>
  )
}