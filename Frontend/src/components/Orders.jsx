import { useState, useEffect } from 'react'
import { fetchOrders, updateOrderStatus } from '../services/api'

const statuses = ['pending','preparing','out-for-delivery','delivered']

export default function OrdersPage(){
  const [orders, setOrders] = useState([])
  useEffect(()=>{load()},[])
  async function load(){
    setOrders(await fetchOrders())
  }
  async function onChange(id, status){
    await updateOrderStatus(id,status)
    load()
  }

  return (
    <div>
      <h2 className="text-2xl font-semibold mb-6">Order Management</h2>
      <div className="space-y-6">
        {orders.map(o=>(
          <div key={o.id} className="bg-white shadow rounded-lg p-6">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-xl font-medium">Order #{o.id}</h3>
              <span className="text-sm text-gray-500">{o.whatsapp_number}</span>
            </div>
            <p className="mb-2"><strong>{o.customer_name}</strong></p>
            <p className="mb-4">Items: {o.items.map(x=>`${x.menu_item_id}×${x.quantity}`).join(', ')}</p>
            <select
              value={o.status}
              onChange={e=>onChange(o.id,e.target.value)}
              className="border rounded p-2"
            >
              {statuses.map(s=>(
                <option key={s} value={s}>{s.replace(/-/g,' ')}</option>
              ))}
            </select>
          </div>
        ))}
      </div>
    </div>
  )
}