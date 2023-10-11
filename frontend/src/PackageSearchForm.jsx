import React, { useState } from 'react'
import axios from './axios'

function PackageSearchForm() {
    const [searchAttribute, setSearchAttribute] = useState('id')
    const [searchTerm, setSearchTerm] = useState('')
    const [searchResult, setSearchResult] = useState(null)

    const handleSearchAttributeChange = (e) => {
        setSearchAttribute(e.target.value)
    }

    const handleSearchTermChange = (e) => {
        setSearchTerm(e.target.value)
    }

    const handleSearch = async (e) => {
        e.preventDefault()

        try {
            const response = await axios.get(`/packages?${searchAttribute}=${searchTerm}`)
            setSearchResult(response.data)
        } catch (error) {
            console.error(error)
            setSearchResult(null)
        }
    }

    return (
        <div>
            <form onSubmit={handleSearch}>
                <label>Search by:</label>
                <select value={searchAttribute} onChange={handleSearchAttributeChange}>
                    <option value="id">ID</option>
                    <option value="return_address">Return Address</option>
                    <option value="destination_address">Destination Address</option>
                </select>
                <input
                    type="text"
                    value={searchTerm}
                    onChange={handleSearchTermChange}
                    placeholder={`Enter ${searchAttribute}`}
                />
                <button type="submit">Search</button>
            </form>

            {searchResult && (
                <div>
                    <h2>Search Results:</h2>
                    <ul>
                        {searchResult.map((pkg) => (
                            <li key={pkg.id}>
                                ID: {pkg.id}<br />
                                Return Address: {pkg.return_address}<br />
                                Destination Address: {pkg.destination_address}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    )
}

export default PackageSearchForm
