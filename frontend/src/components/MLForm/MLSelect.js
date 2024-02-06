import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Select from 'react-select';

const MLSelect = ({ value, onChange }) => {
    const [options, setOptions] = useState([]);
    const [hasMore, setHasMore] = useState(true);
    const [loading, setLoading] = useState(false);
    const [page, setPage] = useState(1);
    const [rgSelected, setRgSelected] = useState({})

    useEffect(() => {
        // Initial load
        fetchOptions(page);
    }, []);

    useEffect(() => {
        if (options.length > 0 && value) {
            findRegion(value);
        }
    }, [options, value]);

    const findRegion = (value) => {
        const option = options.find(option => option.value === value)
        setRgSelected(option)
    }

    const fetchOptions = async (page) => {
        setLoading(true);
        try {
            const response = await axios.get(`get-regions/?page=${page}`);
            const fetchedOptions = response.data.data.map(({ country, region }) => ({
                value: region,
                label: `${country}: ${region}`
            }));

            setOptions((prevOptions) => [...prevOptions, ...fetchedOptions]);
            setHasMore(response.data.has_next);
            // findRegion(value);
        } catch (error) {
            console.error('Error fetching data:', error);
            setHasMore(false);
        } finally {
            setLoading(false);
        }
    };

    const handleScrollToEnd = () => {
        if (!hasMore || loading) return;

        setPage((prevPage) => {
            const nextPage = prevPage + 1;
            fetchOptions(nextPage);
            return nextPage;
        });
    };

    return (
        <Select
            options={options}
            onMenuScrollToBottom={handleScrollToEnd}
            isLoading={loading}
            onChange={onChange}
            value={rgSelected}
            isSearchable
        />
    );
};

export default MLSelect;
