import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import PackageForm from './PackageForm.jsx'
import PackageSearchForm from './PackageSearchForm.jsx'

function App() {
    return (
        <div>
            <h1>Package Management</h1>
            <h2>Create a Package</h2>
            <PackageForm />
            <h2>Search for Packages</h2>
            <PackageSearchForm />
        </div>
    )
}

export default App
