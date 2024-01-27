import React from 'react'
import Grid from '@mui/system/Unstable_Grid'
import { Footer, Header, Main, TopNav } from '../../components'

const Home = () => {

    return (
        <>
            <TopNav />
            <Grid container spacing={2} p={5}>
                <Grid lg={12}>
                    <Header />
                </Grid>
                <Grid lg={12}>
                    <Main />
                </Grid>
                <Grid lg={12}>
                    <Footer />
                </Grid>
            </Grid>
        </>
    )
}

export default Home