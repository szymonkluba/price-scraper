import React from "react";
import moment from "moment";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCheckCircle, faTimesCircle} from "@fortawesome/free-solid-svg-icons";

class PriceTag extends React.Component {
    render() {
        return (
            <div className={'price-tag'}>
                <span className={'price-tag-store'}>{this.props.price.store}</span>
                <span className={'price-tag-price'}>{this.props.price.price} PLN</span>
                <span className={'available'}>{this.props.price.available ?
                    <FontAwesomeIcon icon={faCheckCircle}
                                     size={'lg'}/> :
                    <FontAwesomeIcon icon={faTimesCircle}
                                     size={'lg'}/>}</span>
                <span className={'price-tag-timestamp'}>{moment(this.props.price.timestamp, moment.ISO_8601).fromNow()}</span>
            </div>
        );
    }
}

export default PriceTag