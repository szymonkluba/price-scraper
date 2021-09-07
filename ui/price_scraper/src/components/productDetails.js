import React from "react";
import PriceTag from "./priceTag";
import Thumbnail from "./thumbnail";
import ThumbnailPlaceholder from "./thumbnailPlaceholder";
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
        fetch(url)
            .then(res => res.json())
            .then(
                (result) => {
                    console.log(result)
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
                    console.log(result)
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
    }

    render() {
        const {current_prices, name, url, category, price, timestamp, available, store, image_url} = this.state
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

        let thumbnail;
        if (image_url) {
            thumbnail = <Thumbnail image_url={image_url}/>
        } else {
            thumbnail = <ThumbnailPlaceholder />
        }
        return (
            <div className={'product-details'}>
                {thumbnail}
                <Link to={url}><h1>{name}</h1></Link>
                {prices_list}
                {price_tag}
                <p>{category}</p>
                <button className={"refresh"} onClick={this.updatePrices}><FontAwesomeIcon icon={faSyncAlt} /></button>
            </div>

        )

    }
}

export default ProductDetails