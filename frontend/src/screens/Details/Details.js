import { Grid } from '@mui/material'
import React from 'react'
import { Blog, Footer, TopNav } from '../../components'

const Details = () => {
    return (
        <>
            <TopNav />
            <Grid container spacing={2} p={5}>
                <Grid container spacing={2} p={5} m={5} sx={{ borderRadius: '20px', height: '100%', boxShadow: '0px 5px 22px rgba(0, 0, 0, 0.04), 0px 0px 0px 0.5px rgba(0, 0, 0, 0.03)' }}>
                    <Blog />
                </Grid>
                <Grid lg={12}>
                    <Footer />
                </Grid>
            </Grid>
        </>
    )
}

export default Details