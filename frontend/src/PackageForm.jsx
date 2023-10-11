import React, { useState } from 'react'
import axios from './axios'

function PackageForm() {
    const [formData, setFormData] = useState({
        return_address: '',
        destination_address: '',
        id: '',
    })

    const [message, setMessage] = useState(null) // State to store the success or error message

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const response = await axios.post('/packages', formData)
            setMessage('Package created successfully')
            clearMessageAfterDelay(3000) // Display message for 3 seconds
            console.log(response.data)
        } catch (error) {
            setMessage('Error creating the package')
            clearMessageAfterDelay(3000) // Display message for 3 seconds
            console.error(error)
        }
    }

    const clearMessageAfterDelay = (delay) => {
        setTimeout(() => {
            setMessage(null)
        }, delay)
    }

    return (
        <div>
            {message && <div className="message">{message}</div>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Package ID</label>
                    <input
                        type="text"
                        name="id"
                        value={formData.id}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Return Address</label>
                    <input
                        type="text"
                        name="return_address"
                        value={formData.return_address}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Destination Address</label>
                    <input
                        type="text"
                        name="destination_address"
                        value={formData.destination_address}
                        onChange={handleChange}
                    />
                </div>
                <button type="submit">Create Package</button>
            </form>
        </div>
    )
}

export default PackageForm
