import React, { useEffect, useState } from 'react'
import { Button, Checkbox, FormControl, FormLabel, Grid, InputLabel, MenuItem, Select, TextField } from '@mui/material'
import axios from 'axios';
import MLSelect from './MLSelect';

const MLForm = ({ fetchRestaurants }) => {
    const [formData, setFormData] = useState({
        price_level: '',
        vegetarian_friendly: false,
        vegan_options: false,
        gluten_free: false,
        avg_rating: '',
        region: '',
    });

    const [selectedOption, setSelectedOption] = useState(null);

    useEffect(() => {
        // Fetch the existing preference data when the component mounts
        axios.get('preference/')
            .then((response) => {
                setFormData(response.data);
                setSelectedOption(response.data.region)
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = { ...formData, 'region': selectedOption.value }
        // Send the form data to your Django server
        axios.post('preference/', data)
            .then((response) => {
                if (response.status === 200) {
                    // Success: Preference created
                    console.log('Preference created or updated successfully');
                } else {
                    // Error: Handle errors here
                    console.error('Error creating preference');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            }).finally(() => {
                fetchRestaurants(1)
            });
    };

    const handleChange = (e) => {
        const { name, value, checked, type } = e.target;

        // Handle checkbox inputs separately
        if (type === 'checkbox') {
            setFormData({ ...formData, [name]: checked });
        } else {
            setFormData({ ...formData, [name]: value });
        }

    };
    return (
        <>
            <form onSubmit={handleSubmit}>
                <div style={{
                    display: 'flex', flexDirection: 'row',
                    justifyContent: 'space-around'
                }}>
                    <Grid px={2} sx={{
                        display: 'flex', alignItems: 'center',
                        gap: '2rem'
                    }}>
                        <div>
                            <InputLabel htmlFor="region">Region</InputLabel>
                            <MLSelect value={selectedOption} onChange={(option) => { setSelectedOption(option) }} />
                        </div>
                        <div>
                            <InputLabel htmlFor="price_level">Price Level</InputLabel>
                            <Select
                                name="price_level"
                                value={formData.price_level}
                                onChange={handleChange}
                                fullWidth
                            >
                                <MenuItem value="€">€</MenuItem>
                                <MenuItem value="€€-€€€">€€-€€€</MenuItem>
                                <MenuItem value="€€€€">€€€€</MenuItem>
                            </Select>
                        </div>
                        <div>
                            <InputLabel htmlFor="avg_rating">Average Rating</InputLabel>
                            <Select
                                name="avg_rating"
                                value={formData.avg_rating}
                                onChange={handleChange}
                                fullWidth
                            >
                                <MenuItem value="1">1</MenuItem>
                                <MenuItem value="2">2</MenuItem>
                                <MenuItem value="3">3</MenuItem>
                                <MenuItem value="4">4</MenuItem>
                                <MenuItem value="5">5</MenuItem>
                            </Select>
                        </div>
                    </Grid>
                    <Grid px={2} sx={{
                        display: 'flex', alignItems: 'center'
                    }}>
                        <div>
                            <FormLabel>Vegetarian Friendly</FormLabel>
                            <Checkbox
                                onChange={handleChange}
                                name="vegetarian_friendly"
                                checked={formData.vegetarian_friendly}
                            />
                        </div>
                        <div>
                            <FormLabel>Vegan Options</FormLabel>
                            <Checkbox
                                onChange={handleChange}
                                name="vegan_options"
                                checked={formData.vegan_options}
                            />
                        </div>
                        <div>
                            <FormLabel>Gluten Free</FormLabel>
                            <Checkbox
                                onChange={handleChange}
                                name="gluten_free"
                                checked={formData.gluten_free}
                            />
                        </div>
                    </Grid>
                    <Grid py={2}>
                        <Button variant="outlined" color="secondary" type="submit">Envoyer</Button>
                    </Grid>
                </div>

            </form >
        </>
    )
}

export default MLForm