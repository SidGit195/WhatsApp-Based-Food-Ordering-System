const BASE = 'http://localhost:8000'

export async function fetchMenu(){
  const res = await fetch(`${BASE}/menu`)
  return res.json()
}

export async function addMenu(item){
  const res = await fetch(`${BASE}/menu`, {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify(item)
  })
  return res.json()
}

export async function toggleMenu(id, available){
  const res = await fetch(`${BASE}/menu/${id}`, {
    method:'PATCH',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({available})
  })
  return res.json()
}

export async function fetchOrders(){
  const res = await fetch(`${BASE}/orders`)
  return res.json()
}

export async function updateOrderStatus(id, status){
  const res = await fetch(`${BASE}/orders/${id}`, {
    method:'PATCH',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({status})
  })
  return res.json()
}