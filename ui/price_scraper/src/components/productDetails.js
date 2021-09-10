import React from "react";
import PriceTag from "./priceTag";
import {Link} from "react-router-dom";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faSyncAlt} from "@fortawesome/free-solid-svg-icons";

class ProductDetails extends React.Component {
    constructor(props) {
        super(props);
        this.state = {...props.details};
        this.state.error = null;
        this.updatePrices = this.updatePrices.bind(this)
        this.updateProductDetails = this.updateProductDetails.bind(this)
    }

    updatePrices() {
        const url = window.location.origin.replace('3000', '8000') + this.state.url + 'update_prices/'
        const refreshButton = document.getElementById('refresh-' + this.state.slug);
        refreshButton.classList.add('rotate')
        fetch(url)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        ...result
                    });
                    this.updateProductDetails()
                },
                (error) => {
                    this.setState({
                        error
                    });
                }
            )
    }

    updateProductDetails() {
        const url = window.location.origin.replace('3000', '8000') + this.state.url
        fetch(url)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        ...result
                    });
                },
                (error) => {
                    this.setState({
                        error
                    });
                }
            )
            .finally(() => {
                const refreshButton = document.getElementById('refresh-' + this.state.slug);
                refreshButton.classList.remove('rotate')
            })
    }

    render() {
        const {current_prices, name, slug, url, category, price, timestamp, available, store} = this.state
        let prices_list;
        if (current_prices) {
                prices_list = current_prices.map((price) => <PriceTag key={price.slug} price={price}/>)
            }

        const price_tag = price && <PriceTag price={{
                price: price,
                timestamp: timestamp,
                available: available,
                store: store,
            }} />
        return (
            <div className={'product-details'}>
                <Link to={url}><h1>{name}</h1></Link>
                {prices_list}
                {price_tag}
                <p className={'category'}>{category}</p>
                <button id={"refresh-" + slug} className={"refresh"} onClick={this.updatePrices}><FontAwesomeIcon icon={faSyncAlt} size={'lg'}/></button>
            </div>

        )

    }
}

export default ProductDetails