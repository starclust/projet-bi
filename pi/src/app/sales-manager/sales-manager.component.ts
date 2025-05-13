import { Component } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-sales-manager',
  templateUrl: './sales-manager.component.html',
  styleUrls: ['./sales-manager.component.css']
})
export class SalesManagerComponent {
  showPowerBI: boolean = true;
  showPrediction: boolean = false;
 
  powerBIUrl: SafeResourceUrl;
  predictionUrl: SafeResourceUrl;

  constructor(private sanitizer: DomSanitizer) {
    // Mets ici ton URL Power BI officielle
    this.powerBIUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
      'https://app.powerbi.com/reportEmbed?reportId=6de78771-b132-4f5e-961b-ba0af933b063&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730'
    );

    // Mets ici l'URL de ton serveur Flask déployé
    this.predictionUrl = this.sanitizer.bypassSecurityTrustResourceUrl(
      'http://127.0.0.1:5001'
    );
  }

  showPowerBIView(): void {
    this.showPowerBI = true;
    this.showPrediction = false;
  }

  showPredictionView(): void {
    this.showPowerBI = false;
    this.showPrediction = true;
  }
}
