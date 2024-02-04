import { Grid } from '@mui/material'
import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { Footer, MLContainer, MLForm, TopNav } from '../../components'

const Preference = () => {

    /**
     * rentrer dans la page useEffect -> getRecommendedRestaurants 
     * update Preference -> getRecommendedRestaurants 
     */

    const [loading, setLoading] = useState(false)
    const [restaurants, setRestaurants] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(0);

    const fetchRestaurants = async (page) => {
        setLoading(true)
        try {
            if (!page) {
                page = 1
            }
            const { data } = await axios.get(`get-restaurants/?page=${page}`)
            setRestaurants(data.restaurants)
            setCurrentPage(page)
            setTotalPages(data.total_pages)
        } catch (error) {
            console.error('Error fetching data:', error)
        }
        setLoading(false)
    };

    return (
        <>
            <TopNav />
            <Grid container spacing={2} p={5} sx={{ width: '100%' }}>
                <Grid container spacing={2} p={5} m={5} sx={{ borderRadius: '20px', height: '100%', boxShadow: '0px 5px 22px rgba(0, 0, 0, 0.04), 0px 0px 0px 0.5px rgba(0, 0, 0, 0.03)', display: 'flex', justifyContent: 'center' }}>
                    <MLForm fetchRestaurants={fetchRestaurants} />
                </Grid>
                <Grid container spacing={2} p={5} sx={{ width: '100%', borderRadius: '20px', height: '100%', boxShadow: '0px 5px 22px rgba(0, 0, 0, 0.04), 0px 0px 0px 0.5px rgba(0, 0, 0, 0.03)', display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column' }}>
                    <MLContainer fetchRestaurants={fetchRestaurants}
                        loading={loading}
                        restaurants={restaurants}
                        current={currentPage}
                        totalPages={totalPages} />
                </Grid>
                <Grid lg={12}>
                    <Footer />
                </Grid>
            </Grid>
        </>

    )
}

export default Preference