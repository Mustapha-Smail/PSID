import { CardContent, Divider, Typography, Card, CircularProgress, Alert, CardActions, Button, SvgIcon } from '@mui/material'
import { Stack } from '@mui/system'
import axios from 'axios'
import React, { useEffect, useState } from 'react'
import Plot from 'react-plotly.js'
import ArrowRightIcon from '@heroicons/react/24/solid/ArrowRightIcon'
import PopupData from '../Elements/PopupData'
import Popup from 'reactjs-popup';

const CardGraph = ({ url }) => {
    const [plotData, setPlotData] = useState(null)
    const [plotTitle, setPlotTitle] = useState("")
    const [plotContent, setPlotContent] = useState("")
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    useEffect(() => {
        const getData = async () => {
            try {
                setLoading(true)
                const { data } = await axios.get(`${url}`)
                setPlotData(JSON.parse(data.data))
                setPlotTitle(data.title)
                setPlotContent(data.content)
                setLoading(false)
            } catch (err) {
                setLoading(false)
                setError(err)
                console.error(err)
            }
        }

        getData()
    }, [url])

    return (
        <Card sx={{ borderRadius: '20px', height: '100%', boxShadow: '0px 5px 22px rgba(0, 0, 0, 0.04), 0px 0px 0px 0.5px rgba(0, 0, 0, 0.03)', display: 'flex', flexDirection: 'column' }}>
            <CardContent>
                <Stack spacing={1}>
                    {error && <Alert severity="error">{error.message}</Alert>}
                    {loading ?
                        <Stack p={5} alignItems={"center"} >
                            <CircularProgress />
                        </Stack>
                        :
                        plotData && (
                            <Plot
                                data={plotData.data}
                                layout={{
                                    autosize: true,
                                    title: plotData.layout.title,
                                    responsive: true,
                                    // font: { size: 18 }
                                }}
                                useResizeHandler={true}
                                config={{ responsive: true }} />

                        )
                    }
                </Stack>
            </CardContent>
            <Divider />
            <CardActions sx={{ justifyContent: 'flex-end' }}>
                {plotData && (<Popup
                    trigger={
                        <Button
                            color="inherit"
                            endIcon={(
                                <SvgIcon fontSize="small">
                                    <ArrowRightIcon />
                                </SvgIcon>
                            )}
                            size="small"
                        >
                            Détails
                        </Button>
                    }
                    modal
                    nested
                    contentStyle={{
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        // maxHeight: '50%'

                    }}
                >
                    {close => (
                        <PopupData
                            close={close}
                            title={plotTitle}
                            content={plotContent}
                        />
                    )}
                </Popup>)}
            </CardActions>
        </Card>
    )
}

export default CardGraph