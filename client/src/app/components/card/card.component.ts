import { Component, OnInit } from '@angular/core';
import { Mall } from '../../interfaces/mall';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit {
  mall: Mall = {
    id: 1,
    name: 'Bedok Mall',
    lat: 1.06,
    lon: 5.32,
  };

  img_link = "../../../../../img/" + this.mall.name + ".jpeg";

  constructor() { }

  ngOnInit(): void {
  }

}
